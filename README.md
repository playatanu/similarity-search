# Similarity Image Search

## Overview

This project is a **similarity-based image search system** that enables efficient retrieval of visually similar images from a dataset. It leverages **deep learning** for feature extraction and **FAISS (Facebook AI Similarity Search)** for fast nearest neighbor searches. The system is designed to handle large-scale image datasets efficiently.

### How It Works:

1. **Feature Extraction**: A **ResNet50** model (pre-trained on ImageNet) extracts embeddings (feature vectors) from images.
2. **Indexing with FAISS**: The extracted embeddings are stored in a **FAISS index**, allowing fast similarity searches.
3. **Metadata Storage**: SQLite is used to store image metadata (e.g., file paths, timestamps) and link them to FAISS indices.
4. **Searching for Similar Images**: Given a query image, the system retrieves and ranks the most visually similar images.

### Why Use This?

- **Fast and Scalable**: FAISS ensures rapid search performance even with millions of images.
- **Accurate**: ResNet50 provides robust feature representations.
- **Lightweight Storage**: SQLite efficiently manages metadata without complex database setups.

## Demo

This project is ideal for **reverse image search, content-based recommendation systems,** and **visual search applications**.
