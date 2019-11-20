# This is the forntend part of the project.

Used Tech Stack

## node
## Reactjs
## Apollo Client

## Running on your Machine
First install required node modules by the following command
```
npm install
```
In the project directory, you can run:
```
npm start
```
Runs the app in the development mode.
Open http://localhost:3000 to view it in the browser.

The page will reload if you make edits.
You will also see any lint errors in the console.

```
npm run build
```
Builds the app for production to the build folder.
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.
Your app is ready to be deployed!

Before continuing, the following steps are required:
    1. Get API keys
        ..* Open cloudinary api
            Have a look at [cloudinary](https://cloudinary.com/documentation/image_upload_api_reference) 
    2. Create an app there
    3. Get cloud name,preset from the setting

### Setup envrionment variables
Please follow the following steps:
    1. Add '.env' file
    ...Create a file called '.env' at the root of the application
    2. Add environment variables to '.env' file
    ...REACT_APP_GRAPHQL_API_URL=Your Project Base Url,
    ...REACT_APP_CLOUD_NAME=YOUR_CLOUD_NAME,
    ...REACT_APP_UPLOAD_PRESET=YOUR_PRESET_GOES_HERE,
    ...REACT_APP_CLODUNINARY_URL=YOUR_CLOUDINARY_URL

