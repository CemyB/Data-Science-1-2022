import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Link Analysis - Page Rank")

st.markdown('Here I am analysing a Drug-drug interaction network with the Page Rank algorithm.')

st.header("Data Set")

st.markdown("Here is a brief description of the used dataset.")

st.subheader("Drug-drug interaction network")

st.markdown("This is a network of interactions betweeen drugs, which are approved by the U.S. \
            Food and Drug Administration. Nodes represent drugs and edges represent drug interactions. \
            Drug-drug interactions occur when the pharmacologic effect of a one drug is altered by the \
            action of another drug, leading to unpredictable clinical effects such as adverse drug \
            reactions. When several drugs are administered together, there might be a greater \
            possibility of adverse drug reactions as one drug can increase or decrease the effect \
            of another drug. ")

# read in tsv 
edgelist = pd.read_csv('subset.txt', sep='\t', names=["Node A", "Node B"])

# display data
edgelist

# create graph from edge list
g = nx.read_edgelist("subset.txt", create_using=nx.Graph(),nodetype=str)

# plot data
st.pyplot(fig=nx.draw(g, pos=nx.random_layout(g)))

# show graph info
st.markdown(nx.info(g))

# run basic pagerank 
basic_pr = nx.pagerank(g)

# define personalized vector
personalization_vector = {"DB00862" : 1, "DB00966" : 1, "DB00575" : 1, "DB00806" : 1, "DB01242" : 1}

# run topic specific page rank
specific_pr = nx.pagerank(g, personalization=personalization_vector)

st.header("Results")

st.markdown("Here we see for each node the page rank calculated by the basic and topic-specific page rank algorithm.")

# create data frame with results
node_list = list(g.nodes())
basic_pr_value = list(basic_pr.values())
specific_pr_value = list(specific_pr.values())
my_dict = {"Nodes" : node_list, "Basic PR" : basic_pr_value, "Specific PR" : specific_pr_value}
df = pd.DataFrame(my_dict)

st.markdown("Here is the used personalization vector:")

st.write(personalization_vector)

st.markdown("In order to see the top n page ranks for each algorithm, \
simply click on the column name and sort it descendingly ↓.")

# display data frame
df
