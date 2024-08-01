# Device Price Prediction API

This API, built with Django and Django REST Framework, allows users to manage device data and predict device prices using a machine learning model. The model is a Support Vector Machine (SVM) that predicts the price range of a device based on its specifications.

## API Endpoints

### 1. List all devices
- **URL**: `/devices/`
- **Method**: `GET`
- **Description**: Retrieves a list of all devices.
- **Response**: JSON array of all devices.

### 2. Retrieve a specific device by ID
- **URL**: `/devices/<int:id>/`
- **Method**: `GET`
- **Description**: Retrieves the details of a specific device by its ID.
- **Response**: JSON object of the specified device.

### 3. Add a new device
- **URL**: `/devices/add/`
- **Method**: `POST`
- **Description**: Adds a new device.
- **Request Body**: JSON object with the following device specifications:
  - `battery_power`: Integer (500 - 3000)
  - `blue`: Integer (0 or 1)
  - `clock_speed`: Float (0.1 - 3.0)
  - `dual_sim`: Integer (0 or 1)
  - `fc`: Integer (1 - 90)
  - `four_g`: Integer (0 or 1)
  - `int_memory`: Integer (1 - 90)
  - `m_dep`: Float (0.1 - 1.0)
  - `mobile_wt`: Integer (50 - 90)
  - `n_cores`: Integer (1 - 90)
  - `pc`: Integer (1 - 90)
  - `px_height`: Integer (20 - 3000)
  - `px_width`: Integer (500 - 3000)
  - `ram`: Integer (500 - 3000)
  - `sc_h`: Integer (1 - 90)
  - `sc_w`: Integer (1 - 90)
  - `talk_time`: Integer (1 - 90)
  - `three_g`: Integer (0 or 1)
  - `touch_screen`: Integer (0 or 1)
  - `wifi`: Integer (0 or 1)
- **Response**: JSON object of the newly added device.

### 4. Predict the price of a device
- **URL**: `/predict/`
- **Method**: `POST`
- **Description**: Predicts the price range of a device based on its specifications.
- **Request Body**: JSON object with the device specifications (same as above).
- **Response**: JSON object with the predicted `price_range` (1 - 4).

## Data Preprocessing

The API preprocesses the input data before making predictions. The preprocessing steps include:
1. **Binary Feature Conversion**: Converts binary features (e.g., `blue`, `dual_sim`) into a single decimal feature.
2. **Feature Engineering**: Creates new features such as `pixel_area`, `screen_area`, and `pcfc` (product of `pc` and `fc`).
3. **Scaling**: Scales the integer features using `StandardScaler`.

## Machine Learning Model

The price prediction is performed using a pre-trained Support Vector Machine (SVM) model. The model is loaded using `joblib` and predicts the price range based on the preprocessed device specifications.
