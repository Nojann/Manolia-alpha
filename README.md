![Manolia logo](./doc/manolia.png?raw=true)

https://www.manolia.org/

## About The Project

Manolia provides a knowledge layer for Natural Language Processing, centered on commons-based peer production and sustainability. It serves as an intermediary layer between collective knowledge system and lightweight, open-source NLP tools, designed to process raw and unstructured knowledge into structured, well-designed formats for collaborative work. This enables the creation of effective digital commons. The system is aimed at communities that prioritize privacy and sustainability and requires small-scale and quality automation of knowledge processing.

## Built With

UI: Vue.js
Server: FastAPI

## Small Language Model

Inference Engine: llama.cpp
Model: SmolLM3
Hardware tested : CPU Intel Xeon E5430

# Alpha
At this early stage, Manolia is an annotation application. It enables data to be collected on users’ perceptions of the quality of the questions generated from a paragraph of knowledge entered by the user.

# Beta

Objective: To build an API server containing a complete pipeline. 

![Component diagram](./doc/component_diagram.png?raw=true "Component diagram")
![NLP pipeline](./doc/nlp_pipeline.png?raw=true "NLP pipeline")