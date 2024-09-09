//react-vite/src/redux/product.js
const ADD_PRODUCT = 'products/addProductOne';
const DELETE_PRODUCT = "products/deleteProductOne"
const LOAD_PRODUCTS_ALL = "products/loadProductsAll"
const LOAD_PRODUCTS_ONE = "products/loadProductsOne"
const LOAD_PRODUCTS_OWNED = "products/loadProductsOwned"
const UPDATE_PRODUCT = "products/updateProductOne"


// Actions
const addProduct = (data) => ({
    type: ADD_PRODUCT,
    payload: data
})

const deleteProduct = (data) => ({
    type: DELETE_PRODUCT,
    payload: data
})

const loadProductsAll = (data) => {
    return {
        type: LOAD_PRODUCTS_ALL,
        payload: data
    };
};

const loadProductsOne = (data) => {
    return {
        type: LOAD_PRODUCTS_ONE,
        payload: data
    };
};

const loadProductsOwned = (data) => {
    return {
        type: LOAD_PRODUCTS_OWNED,
        payload: data,
    };
};

const updateProduct = (data) => ({
    type: UPDATE_PRODUCT,
    payload: data
})

//Thunks
export const addProductThunk = (product) => async (dispatch) => {
    const { body, imageURLs } = product;
    const response = await csrfFetch("/api/products", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
    });
    const data = await response.json();
    await insertProductImages({ productId: data.id, imageURLs});
    if (response.ok) {
        dispatch(addProduct(data))
        return data.id
    }
}

export const deleteProductThunk = (productId) => async (dispatch) => {
    const response = await csrfFetch(`/api/products/${productId}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
    });

    if (response.ok) {
        const data = await response.json()
        dispatch(deleteProduct(productId))
        return data
    }
}

export const getProductsAllThunk = () => async (dispatch) => {
    const response = await csrfFetch('/api/products')
    if (response.ok) {
        const data = await response.json();
        dispatch(loadProductsAll(data))
        return data
    }
}

export const getProductsOwnedThunk = () => async (dispatch) => {
    const response = await csrfFetch("/api/products/current");
    if (response.ok) {
        const data = await response.json();
        dispatch(loadProductsOwned(data));
    }
};

export const getProductsOneThunk = (productId) => async (dispatch) => {
    const response = await csrfFetch(`/api/products/${productId}`)
    if (response.ok) {
        const data = await response.json();
        dispatch(loadProductsOne(data))
        return data
    }
}

export const updateProductThunk = (product) => async (dispatch) => {
    const { body, imageURLs, productId } = product;
    await deleteSpotImages(productId);
    const response = await csrfFetch(`/api/products/${productId}`, {
        method: 'PUT',
        header: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
    })
    const data = await response.json();
    await insertProductImages({ productId: data.id, imageURLs });
    if (response.ok) {
        dispatch(updateProduct(data))
        return data.id
    }
}


const insertProductImages = async ({ productId, imageURLs }) => {
    // post side images
    for (let url of imageURLs) {
        await csrfFetch(`/api/products/${productId}/images`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ url, productId}),
        });
    }
};

const deleteSpotImages = async (productId) => {
    await csrfFetch(`/api/product-images/spot/${productId}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
    });
};

// State Object
const initialState = { user: null };

// Reducers
function productReducer(state = initialState, action) {
  switch (action.type) {
    case ADD_PRODUCT: {
        let newState = { ...state }
        newState.allProducts = [...newState.allProducts, action.payload]
        newState.byId[action.payload.id] = action.payload;
        newState.single = action.payload;
        return newState;
    }

    case DELETE_PRODUCT: {
        let newState = { ...state }
        newState.allProducts = newState.allProducts.filter(product => product.id !== action.payload);
        delete newState.byId[action.payload];

        if (newState.single.id === action.payload) {
            newState.single = {};
        }
        return newState
    }

    case LOAD_PRODUCTS_ALL: {
        let newState = { ...state }
        newState.allProducts = action.payload.Products;
        for (let product of action.payload.Products) {
            newState.byId[product.id] = product
        }
        return newState;
    }

    case LOAD_PRODUCTS_ONE: {
        let newState = { ...state }
        newState.single = action.payload
        return newState
    }

    case LOAD_PRODUCTS_OWNED: {
        let newState = { ...state }
        newState.allProducts = action.payload.Products;
        for (let product of action.payload.Products) {
            newState.byId[product.id] = product
        }
        return newState;
    }

    case UPDATE_PRODUCT: {
        let newState = { ...state }

        const reviewId = action.payload.id

        const newAllProducts = [];

        for (let i = 0; i < newState.allProducts.length; i++){
            let currentReview = newState.allProducts[i]
            if (currentReview.id === reviewId){
                newAllProducts.push(action.payload)
            } else {
                newAllProducts.push(currentReview)
            }
        }

        newState.allProducts = newAllProducts
        newState.byId = {...newState.byId, [reviewId]: action.payload}
        return newState
    }

    default:
      return state;
  }
}

export default productReducer;