//Constants
const GET_PRODUCT_IMAGES = 'GET_PRODUCT_IMAGES';
// const GET_PRODUCT_IMAGE = 'GET_PRODUCT_IMAGE';
const CREATE_PRODUCT_IMAGE = 'CREATE_PRODUCT_IMAGE';
const DELETE_PRODUCT_IMAGE = 'DELETE_PRODUCT_IMAGE';
// const UPDATE_PRODUCT_IMAGE = 'UPDATE_PRODUCT_IMAGE';

//Action Creators
const getProductImages = (productImages) => ({
    type: GET_PRODUCT_IMAGES,
    payload: productImages
});

const createProductImage = (productImage) => ({
    type: CREATE_PRODUCT_IMAGE,
    payload: productImage
});

const deleteProductImage = (productImageId) => ({
    type: DELETE_PRODUCT_IMAGE,
    payload: productImageId
});

// const updateProductImage = (productImage) => ({
//     type: UPDATE_PRODUCT_IMAGE,
//     payload: productImage
// });

//Thunks
export const getProductImagesThunk = (productId) => async (dispatch) => {
    const response = await fetch(`/api/products/${productId}/images`);

    if (response.ok) {
        const productImages = await response.json();
        dispatch(getProductImages(productImages));
    }
};

export const createProductImageThunk = (productImage, productId) => async (dispatch) => {
    const response = await fetch(`/api/products/${productId}/images`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(productImage)
    });

    if (response.ok) {
        const productImage = await response.json();
        dispatch(createProductImage(productImage));
    }
};

export const deleteProductImageThunk = (productImageId) => async (dispatch) => {
    const response = await fetch(`/api/images/${productImageId}`, {
        method: 'DELETE'
    });

    if (response.ok) {
        dispatch(deleteProductImage(productImageId));
    }
};

//Reducer
