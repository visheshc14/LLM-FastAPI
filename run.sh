#!/bin/bash

# Step 1: Training the model
python trainer.py --fp dataset.txt --output_dir model_weights --max_epochs 10 &

# Step 2: Serving the model over FastAPI
python server.py &

# Wait for the server to start
sleep 5

# Step 3: Calling the model via cURL
curl -X POST "http://localhost:8000/generate_text" -H "Content-Type: application/json" -d '{"text":"Hello, model!"}'
