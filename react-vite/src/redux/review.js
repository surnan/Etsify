
//react-vite/src/redux/product.js
const ADD_REVIEW = 'reviews/addReviewOne';
const DELETE_REVIEW = "reviews/deleteReviewOne"
const LOAD_REVIEWS_ALL = "reviews/loadReviewsAll"
const UPDATE_REVIEW = "reviews/updateReviewOne"


// Actions
const addReview = (data) => ({
    type: ADD_REVIEW,
    payload: data
})

const deleteReview = (data) => ({
    type: DELETE_REVIEW,
    payload: data
})

const loadReviewsAll = (data) => {
    return {
        type: LOAD_REVIEWS_ALL,
        payload: data
    };
};



const updateReview = (data) => ({
    type: UPDATE_REVIEW,
    payload: data
})

//Thunks
export const addReviewThunk = (rev) => async (dispatch) => {
    const {stars, review, userId, productId } = rev;
    const response = await fetch("/api/reviews", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
    });
    const data = await response.json();
    // await insertProductImages({ productId: data.id, imageURLs });
    if (response.ok) {
        dispatch(addReview(data))
        return data.id
    }
}

export const deleteReviewThunk = (reviewId) => async (dispatch) => {
    const response = await fetch(`/api/reviews/${reviewId}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
    });

    if (response.ok) {
        const data = await response.json()
        dispatch(deleteReview(reviewId))
        return data
    }
}

export const getReviewsAllThunk = () => async (dispatch) => {
    const response = await fetch('/api/reviews')
    if (response.ok) {
        const data = await response.json();
        dispatch(loadReviewsAll(data))
        return data
    }
}

export const updateReviewThunk = (rev) => async (dispatch) => {
    const {stars, review, userId, productId } = rev;
    // await deleteSpotImages(productId);
    const response = await fetch(`/api/reviews/${reviewId}`, {
        method: 'PUT',
        header: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
    })
    const data = await response.json();
    // await insertProductImages({ reviewtId: data.id, imageURLs });
    if (response.ok) {
        dispatch(updateReview(data))
        return data.id
    }
}




// State Object
const initialState = { user: null };

// Reducers
function reviewReducer(state = initialState, action) {
    switch (action.type) {
        case ADD_REVIEW: {
            let newState = { ...state }
            newState.allReviews = [...newState.allReviews, action.payload]
            newState.byId[action.payload.id] = action.payload;
            newState.single = action.payload;
            return newState;
        }

        case DELETE_REVIEW: {
            let newState = { ...state }
            newState.allReviews = newState.allReviews.filter(review => review.id !== action.payload);
            delete newState.byId[action.payload];

            if (newState.single.id === action.payload) {
                newState.single = {};
            }
            return newState
        }

        case LOAD_REVIEWS_ALL: {
            let newState = { ...state }
            newState.allReviews = action.payload.Reviews;
            for (let review of action.payload.Reviews) {
                newState.byId[review.id] = review
            }
            return newState;
        }

        case UPDATE_REVIEW: {
            let newState = { ...state }

            const reviewId = action.payload.id

            const newAllReviews = [];

            for (let i = 0; i < newState.allReviews.length; i++) {
                let currentReview = newState.allReviews[i]
                if (currentReview.id === reviewId) {
                    newAllReviews.push(action.payload)
                } else {
                    newAllReviews.push(currentReview)
                }
            }

            newState.allReviews = newAllReviews
            newState.byId = { ...newState.byId, [reviewId]: action.payload }
            return newState
        }

        default:
            return state;
    }
}

export default reviewReducer;
