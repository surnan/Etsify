//Constants
const GET_PRODUCT_IMAGES = 'GET_PRODUCT_IMAGES';
// const GET_PRODUCT_IMAGE = 'GET_PRODUCT_IMAGE';
const CREATE_PRODUCT_IMAGE = 'CREATE_PRODUCT_IMAGE';
const DELETE_PRODUCT_IMAGE = 'DELETE_PRODUCT_IMAGE';
const UPDATE_PRODUCT_IMAGE = 'UPDATE_PRODUCT_IMAGE';

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
// export const getProductImagesThunk = (productId) => async (dispatch) => {
//     const response = await fetch(`/api/products/${productId}/images`);

//     if (response.ok) {
//         const productImages = await response.json();
//         dispatch(getProductImages(productImages));
//     }
// };
export const getProductImagesThunk = (productId) => async (dispatch) => {
    try {
        const response = await fetch(`/api/products/${productId}/images`);
        if (response.ok) {
            const productImages = await response.json();
            dispatch(getProductImages(productImages));
        } else {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to fetch product images');
        }
    } catch (error) {
        console.error('Error fetching product images:', error);
    }
};

// export const createProductImageThunk = (productImage, productId) => async (dispatch) => {
//     const response = await fetch(`/api/products/${productId}/images`, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(productImage)
//     });

//     if (response.ok) {
//         const productImage = await response.json();
//         dispatch(createProductImage(productImage));
//     }
// };

export const createProductImageThunk = (productImage, productId) => async (dispatch) => {
    try {
        const response = await fetch(`/api/products/${productId}/images`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(productImage),
        });

        if (response.ok) {
            const newProductImage = await response.json();
            dispatch(createProductImage(newProductImage));
        } else {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to create product image');
        }
    } catch (error) {
        console.error('Error creating product image:', error);
    }
};


// export const deleteProductImageThunk = (productImageId) => async (dispatch) => {
//     const response = await fetch(`/api/images/${productImageId}`, {
//         method: 'DELETE'
//     });

//     if (response.ok) {
//         dispatch(deleteProductImage(productImageId));
//     }
// };

export const deleteProductImageThunk = (productImageId) => async (dispatch) => {
    try {
        const response = await fetch(`/api/images/${productImageId}`, {
            method: 'DELETE',
        });

        if (response.ok) {
            dispatch(deleteProductImage(productImageId));
        } else {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to delete product image');
        }
    } catch (error) {
        console.error('Error deleting product image:', error);
    }
};

const initialState = { allReviews: [], byId: {} };

//Reducer
const productImageReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_PRODUCT_IMAGES: {
            const newState = { ...state };
            newState.images = action.payload;
            action.payload.forEach((image) => {
                newState.byId[image.id] = image;
            });
            return newState;
        }
        case CREATE_PRODUCT_IMAGE: {
            const newState = { ...state };
            newState.images = [...newState.images, action.payload];
            newState.byId[action.payload.id] = action.payload;
            return newState;
        }
        case DELETE_PRODUCT_IMAGE: {
            const newState = { ...state };
            newState.images = newState.images.filter(
                (image) => image.id !== action.payload
            );
            delete newState.byId[action.payload];
            return newState;
        }
        case UPDATE_PRODUCT_IMAGE: {
            const newState = { ...state };
            newState.byId[action.payload.id] = action.payload;
            newState.images = newState.images.map((image) =>
                image.id === action.payload.id ? action.payload : image
            );
            return newState;
        }
        default:
            return state;
    }
};

export default productImageReducer;