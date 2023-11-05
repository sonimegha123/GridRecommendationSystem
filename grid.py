import itertools
import pandas as pd
import streamlit as st
import pandas as pd
import itertools
import matplotlib.pyplot as plt
from itertools import combinations
import random

'''New Combined Method:
If the "Get Recommendations" button is pressed:
Check if the user has entered more than 3 items.

If they have:
First Phase (from Code 2): Split the user's inputs exactly in half and display recommendations for each half. This gives a focused recommendation based on two broad groups.

Second Phase (Custom): Choose a few (e.g., 2 or 3) random or strategically selected split points, other than the exact half. For each of these splits, get and display recommendations for both halves. This introduces an element of variety and covers more combinations of user inputs.

Final Phase (from Code 1): Finally, get recommendations for the entire list of user inputs and display them. This ensures that the overall preferences are considered.

If the user has entered 3 items or less:

Get recommendations for the entire list of user inputs and display them.'''



data = {
    ('Paragraph', '1.1'): {'25%': True, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Paragraph', '1.2'): {'25%': False, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Paragraph', '1.3'): {'25%': False, '33%': False, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Paragraph', '1.4'): {'25%': False, '33%': False, '50% V': False, '50% H': True, '67%': True, '100%': False},
    ('Paragraph', '1.5'): {'25%': False, '33%': False, '50% V': False, '50% H': False, '67%': True, '100%': False},
    ('Bullet Point (Headings Only)', '2a.1.L'): {'25%': True, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Bullet Point (Headings Only)', '2a.2.L'): {'25%': False, '33%': True, '50% V': True, '50% H': False, '67%': True, '100%': False},
    ('Bullet Point (Headings Only)', '2a.1.G'): {'25%': False, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('Bullet Point (Headings Only)', '2a.2.G'): {'25%': False, '33%': False, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('Bullet Point (Headings Only)', '2a.3.G'): {'25%': False, '33%': False, '50% V': False, '50% H': False, '67%': True, '100%': False},
    ('Bullet Point (Headings Only)', '2a.4.G'): {'25%': False, '33%': False, '50% V': False, '50% H': False, '67%': True, '100%': False},
    ('Bullet Point (Heading + Body)', '2b.1.L'): {'25%': True, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Bullet Point (Heading + Body)', '2b.2.L'): {'25%': False, '33%': True, '50% V': True, '50% H': False, '67%': True, '100%': False},
    ('Bullet Point (Heading + Body)', '2b.1.G'): {'25%': False, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('Bullet Point (Heading + Body)', '2b.2.G'): {'25%': False, '33%': False, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('Bullet Point (Heading + Body)', '2b.3.G'): {'25%': False, '33%': False, '50% V': False, '50% H': False, '67%': False, '100%': True},
    ('Image', '3.1'): {'25%': False, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('Image', '3.2'): {'25%': False, '33%': False, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('Image', '3.3'): {'25%': False, '33%': False, '50% V': False, '50% H': True, '67%': True, '100%': False},
    ('Image', '3.4'): {'25%': False, '33%': False, '50% V': False, '50% H': False, '67%': True, '100%': False},
    ('Table', '4.1'): {'25%': True, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Table', '4.2'): {'25%': False, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Table', '4.3'): {'25%': False, '33%': False, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Table', '4.4'): {'25%': False, '33%': False, '50% V': False, '50% H': False, '67%': True, '100%': True},
    ('Graph', '5.1a'): {'25%': False, '33%': False, '50% V': True, '50% H': False, '67%': True, '100%': True},
    ('Graph', '5.1b'): {'25%': False, '33%': False, '50% V': True, '50% H': False, '67%': True, '100%': True},
    ('Graph', '5.1c'): {'25%': True, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Graph', '5.1d'): {'25%': False, '33%': False, '50% V': True, '50% H': False, '67%': True, '100%': True},
    ('Quote', '6.1'): {'25%': True, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': True},
    ('Quote', '6.2'): {'25%': False, '33%': True, '50% V': True, '50% H': False, '67%': True, '100%': False},
    ('Quote', '6.3'): {'25%': False, '33%': True, '50% V': True, '50% H': False, '67%': True, '100%': False},
    ('List', '7.1'): {'25%': False, '33%': True, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('List', '7.2'): {'25%': False, '33%': False, '50% V': True, '50% H': True, '67%': True, '100%': False},
    ('List', '7.3'): {'25%': False, '33%': False, '50% V': False, '50% H': True, '67%': True, '100%': False},
    ('List', '7.4'): {'25%': False, '33%': False, '50% V': False, '50% H': False, '67%': True, '100%': False},
    ('Cycle', '8.1'): {'25%': False, '33%': True, '50% V': True, '50% H': False, '67%': True, '100%': True},
    ('Process', '9.1'): {'25%': False, '33%': False, '50% V': False, '50% H': True, '67%': True, '100%': True},
    ('Timeline', '10.1'): {'25%': False, '33%': False, '50% V': False, '50% H': True, '67%': True, '100%': True},
    ('Funnel', '11.1'): {'25%': False, '33%': True, '50% V': True, '50% H': False, '67%': True, '100%': True},
    ('Pyramid', '12.1'): {'25%': False, '33%': True, '50% V': True, '50% H': False, '67%': True, '100%': True},
}


# Create a MultiIndex from the tuple keys
index = pd.MultiIndex.from_tuples(data.keys(), names=["Element", "Subset"])

# Create the DataFrame
df = pd.DataFrame(data.values(), index=index)

data = {
    "Weights": [0.5, 0.5, 0.5, 0.5, 0.5, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.6, 0.6, 0.6, 0.6, 0.6, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.5, 0.9, 0.9, 0.6, 0.6],
    "Combined Weight": [0.25, 0.25, 0.25, 0.4, 0.5, 0.15, 0.3, 0.12, 0.18, 0.18, 0.3, 0.3, 0.6, 0.3, 0.42, 0.6, 0.16, 0.16, 0.24, 0.36, 0.2, 0.2, 0.28, 0.36, 0.2, 0.2, 0.12, 0.20, 0.36, 0.48, 0.6, 0.35, 0.49, 0.63, 0.7, 0.5, 0.9, 0.9, 0.6, 0.6],
    "subset": ["1.1", "1.2", "1.3", "1.4", "1.5", "2a.1.L", "2a.2.L", "2a.1.G", "2a.2.G", "2a.3.G", "2a.4.G", "2b.1.L", "2b.2.L", "2b.1.G", "2b.2.G", "2b.3.G", "3.1", "3.2", "3.3", "3.4", "4.1", "4.2", "4.3", "4.4", "5.1a", "5.1b", "5.1c", "5.1d", "6.1", "6.2", "6.3", "7.1", "7.2", "7.3", "7.4", "8.1", "9.1", "10.1", "11.1", "12.1"]
}

# Convert the dictionary to a pandas DataFrame
df_2 = pd.DataFrame(data)


def assign_weights(df_2, user_inputs, combinations):
    """
    Assign weights to user_inputs based on the data in df_2.
    
    Parameters:
    - df_2: DataFrame containing the weights.
    - user_inputs: List of user inputs to be sorted.
    - combinations: Recommendations to map to sorted inputs.

    Returns:
    A dictionary mapping user inputs to recommendations.
    """
    sorted_inputs = sorted(user_inputs, key=lambda x: df_2.set_index('subset')['Combined Weight'].get(x[1], 0), reverse=True)
    sorted_recommendations = sorted(combinations, key=lambda x: int(x.rstrip('% V H')), reverse=True)
    return {element[0]: recommendation for element, recommendation in zip(sorted_inputs, sorted_recommendations)}

def recommend_grids(df, df_2, user_inputs):
    """
    Recommend grids based on user input.

    Parameters:
    - df: DataFrame containing available grid combinations.
    - df_2: DataFrame containing weights.
    - user_inputs: List of tuples containing user input.

    Returns:
    A list of dictionaries containing recommended grids.
    """
    user_subsets = [t[1] for t in user_inputs]
    user_rows = df.loc[user_inputs]
    available_percentages = [row.index[row].tolist() for _, row in user_rows.iterrows()]
    all_combinations = list(itertools.product(*available_percentages))

    valid_combinations = [combo for combo in all_combinations if sum(int(percent.split('%')[0]) for percent in combo) in (100, 99)]

    if len(user_subsets) == 1:
        #return [{'0%': '100%'}]
        return [{user_inputs[0][0]: '100%'}]

    # Filter out symmetric combinations
    def is_symmetric(combination):
        return (combination[0], combination[1]) not in [('50% V', '50% H'), ('50% H', '50% V'), ('25% V', '25% H')]
   
    valid_combinations = list(filter(is_symmetric, valid_combinations))

    if valid_combinations:
        return [assign_weights(df_2, user_inputs, combo) for combo in valid_combinations]
    else:
        subset_weights = df_2[df_2['subset'].isin(user_subsets)]['Combined Weight']
        highest_weight_element = subset_weights.idxmax()
        top_subset = df_2['subset'][highest_weight_element]
        st.subheader(f"""For {top_subset}, the recommended grid is 100% """)
        other = [t for t in user_inputs if t[1] != top_subset]
        return recommend_grids(df, df_2, other)

def split_combinations(lst):
    if not lst:
        return [[]]
    combinations = []
    for i in range(1, len(lst)):
        for combo in split_combinations(lst[i:]):
            combinations.append([lst[:i]] + combo)
    return combinations

# Define the Streamlit app
def main():
    st.title("Grid Recommendation App")

    # User input section
    st.sidebar.header("User Input")

    # Multi-select for selecting elements
    selected_elements = st.sidebar.multiselect(
        "Select Elements",
        df.index.get_level_values('Element').unique(),
        default=[]  # Initially, no elements are selected
    )

    user_inputs = []  # Initialize an empty list for user inputs

    # Display selected elements
    st.sidebar.header("Selected Elements")
    for element in selected_elements:
        st.sidebar.write(f"Element: {element}")

    # For each selected element, allow selection of subsets
    for element in selected_elements:
        available_subsets = df.loc[element].index.tolist()
        subset = st.sidebar.selectbox(f"Select Subset for {element}", available_subsets, key=element)
        user_inputs.append((element, subset))


    # Display user inputs
    st.sidebar.header("Selected Inputs")
    for user_input in user_inputs:
        st.sidebar.write(f"Element: {user_input[0]}, Subset: {user_input[1]}")

    if st.sidebar.button("Get Recommendations"):
    # Check if user inputs have more than 3 elements
        if len(user_inputs) > 3:
        # Split in half (from Code 2)
            split_index = len(user_inputs) // 2
            halves = [(user_inputs[:split_index], user_inputs[split_index:])]
        
        # Additional splits: Choose 2 random split points
            random_splits = random.sample(range(1, len(user_inputs)), 2)
            for split in random_splits:
                halves.append((user_inputs[:split], user_inputs[split:]))

        # Display recommendations for each split
            for first_half, second_half in halves:
                st.subheader(f"Recommendations for Split {len(first_half)}-{len(second_half)}:")
                recommendations_first_half = recommend_grids(df, df_2, first_half)
                recommendations_second_half = recommend_grids(df, df_2, second_half)
            
                display_recommendations(recommendations_first_half)
                display_recommendations(recommendations_second_half)

        # Final recommendations for the entire list (from Code 1)
            recommendations = recommend_grids(df, df_2, user_inputs)
            display_recommendations(recommendations)
        else:
            recommendations = recommend_grids(df, df_2, user_inputs)
            display_recommendations(recommendations)

# Function to display the recommended grid as pie charts
def display_recommendations(recommendations):
    if len(recommendations) == 0:
        st.error("No valid recommendations found.")
    else:
        st.success("Unique Recommended Grids:")
        for i, recommendation in enumerate(recommendations, start=1):
            st.subheader(f"Recommendation {i}")
            display_grid(recommendation)

# Function to display the recommended grid as a pie chart
def display_grid(recommendation):
    fig, ax = plt.subplots(figsize=(6, 4))
    percentages = [int(percent.split('%')[0]) for percent in recommendation.values()]
    labels = recommendation.keys()
    ax.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
