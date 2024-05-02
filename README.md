# BotanicSightMajor


- **models/**: Directory containing the TensorFlow.js model file (`model.json`).
- **src/**: Directory containing the project's source code.
  - **inference.js**: Main JavaScript file for running inference in Node.js.
  - **utils.js**: Utility functions (if needed).
- **python/**: Directory containing the Python script (`model_server.py`) to serve the TensorFlow model.
- **package.json**: Project configuration file specifying dependencies and scripts.

## Usage

1. **Convert Python Model to TensorFlow.js (Optional)**:
   - If your Python model is in TensorFlow format, you can convert it to TensorFlow.js format using `tensorflowjs_converter`.
   - Run `tensorflowjs_converter --input_format=tf_saved_model --output_format=tfjs_graph_model /path/to/python_model /path/to/output_directory`.

2. **Run Python Model Server**:
   - Navigate to the `python/` directory.
   - Run `python model_server.py` to start the server.

3. **Run Node.js Inference Script**:
   - Navigate to the project root directory.
   - Run `npm install` to install dependencies.
   - Run `node src/inference.js` to perform inference using the TensorFlow.js model.

## Dependencies

- TensorFlow.js: `npm install @tensorflow/tfjs`
- Flask (Python): `pip install flask`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
