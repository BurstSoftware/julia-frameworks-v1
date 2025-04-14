import streamlit as st

# Define the framework categories and their respective frameworks
frameworks_data = {
    "General-Purpose and Web Frameworks": [
        "Genie.jl - A full-stack web framework for modern applications",
        "HTTP.jl - Handles HTTP requests and responses",
        "Oxygen.jl - Lightweight framework for RESTful APIs"
    ],
    "Machine Learning and Data Science": [
        "Flux.jl - Flexible neural network framework",
        "MLJ.jl - Unified interface for machine learning models",
        "Knet.jl - Deep learning with GPU support",
        "ScikitLearn.jl - Wrapper for Python's Scikit-Learn"
    ],
    "Scientific Computing and Numerical": [
        "DifferentialEquations.jl - Solves various differential equations",
        "JuMP.jl - Mathematical optimization modeling",
        "Optim.jl - Numerical optimization tools"
    ],
    "Data Manipulation and Analysis": [
        "DataFrames.jl - Tabular data manipulation",
        "Query.jl - Expressive data querying",
        "Tidier.jl - Tidyverse-inspired data wrangling"
    ],
    "Visualization": [
        "Plots.jl - Unified plotting interface",
        "Gadfly.jl - Statistical plotting like ggplot2",
        "Makie.jl - Advanced 2D/3D interactive plotting"
    ],
    "Parallel and Distributed Computing": [
        "Distributed.jl - Parallel computing framework",
        "MPI.jl - Message Passing Interface support",
        "CUDA.jl - GPU programming with NVIDIA CUDA"
    ],
    "Signal and Image Processing": [
        "Images.jl - Image manipulation and analysis",
        "DSP.jl - Digital signal processing",
        "Wavelets.jl - Wavelet transforms"
    ],
    "Testing and Development": [
        "Test.jl - Unit testing framework",
        "BenchmarkTools.jl - Performance benchmarking",
        "Revise.jl - Live code updating"
    ],
    "Statistics and Probabilistic Programming": [
        "StatsBase.jl - Basic statistical functions",
        "Distributions.jl - Probability distributions",
        "Turing.jl - Bayesian inference"
    ],
    "Mathematical and Symbolic Computing": [
        "Symbolics.jl - Symbolic computation",
        "LinearAlgebra.jl - Optimized linear algebra",
        "SpecialFunctions.jl - Special mathematical functions"
    ]
    # You can expand this dictionary with more categories and frameworks from the previous lists
}

# Streamlit app
def main():
    # Title of the app
    st.title("Julia Frameworks Explorer")

    # Dropdown menu at the top of the main app
    selected_category = st.selectbox(
        "Select a Framework Category",
        options=list(frameworks_data.keys()),
        index=0  # Default to the first category
    )

    # Display the list of frameworks for the selected category
    st.subheader(f"Frameworks in {selected_category}")
    frameworks = frameworks_data[selected_category]
    
    if frameworks:
        for framework in frameworks:
            st.write(f"- {framework}")
    else:
        st.write("No frameworks available in this category.")

if __name__ == "__main__":
    main()
