//Constants
const GET_REVIEWS = 'review/GET_REVIEWS';
const GET_REVIEW = 'review/GET_REVIEW';
const ADD_REVIEW = 'review/ADD_REVIEW';
const DELETE_REVIEW = 'review/DELETE_REVIEW';
const EDIT_REVIEW = 'review/EDIT_REVIEW';
//mama
//Action Creators
const getReviews = (reviews) => ({
    type: GET_REVIEWS,
    payload: reviews
});

const getReview = (review) => ({
    type: GET_REVIEW,
    payload: review
});

const addReview = (review) => ({
    type: ADD_REVIEW,
    payload: review
});

const deleteReview = (deletedReview) => ({
    type: DELETE_REVIEW,
    payload: deletedReview
});

const editReview = (updatedReview) => ({
    type: EDIT_REVIEW,
    payload: updatedReview
});

//Thunks
export const getReviewsThunk = (productId) => async (dispatch) => {
    const response = await fetch(`/api/products/${productId}/reviews`);

    if (response.ok) {
        const reviews = await response.json();
        console.log(reviews)
        dispatch(getReviews(reviews));
    }
};

export const getReviewThunk = (reviewId) => async (dispatch) => {
    const response = await fetch(`/api/reviews/${reviewId}`);

    if (response.ok) {
        const review = await response.json();
        dispatch(getReview(review));
    }
};

export const addReviewThunk = (review, productId, userId) => async (dispatch) => {

    const response = await fetch(`/api/reviews/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "stars":review.stars,
            "review": review.review,
            "productId": productId,
            "userId": userId
        })
    });

    console.log('The response is', response)

    if (response.ok) {
        const data = await response.json();
        
        dispatch(addReview(data));
        return data;
    }
};

export const deleteReviewThunk = (reviewId) => async (dispatch) => {
    const response = await fetch(`/api/reviews/${reviewId}`, {
        method: 'DELETE'
    });

    if (response.ok) {
        dispatch(deleteReview(reviewId));
    }
};

export const editReviewThunk = (review) => async (dispatch) => {
    console.log('The edited review is ', review)
    const response = await fetch(`/api/reviews/${review.id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(review)
    });

    if (response.ok) {
        const review = await response.json();

        dispatch(editReview(review));
    }
};


//Reducer
const initialState = {};

function reviewReducer(state = initialState, action) {
    let newState;

    switch (action.type) {
        case GET_REVIEWS: {
            newState = { ...state };
            newState.allReviews = action.payload;
            for (let review of newState.allReviews) {
                newState.byId[review.id] = review;
            }
            return newState;
        }

        case GET_REVIEW: {
            newState = { ...state };
            newState.currentReview = action.payload;
            return newState;
        }

        case ADD_REVIEW: {
            newState = { ...state };
            newState.allReviews = {...action.payload};
            console.log('Mary has a ', newState, ' lamb')
            newState.byId = { ...newState.byId, [action.payload.id]: action.payload };
            return newState;
        }

        case EDIT_REVIEW: {
            newState = { ...state };
            const reviewId = action.payload.id;

            const newAllReviews = [];
            console.log('The state is....... ', newState)

            newAllReviews.push(action.payload);
               
            newState.allReviews = newAllReviews;
            console.log('All Reviews is', newState.allReviews)
            newState.byId = { ...newState.byId, [reviewId]: action.payload };

            return newState;
        }

        case DELETE_REVIEW: {
            newState = { ...state };

            const filteredReviews = newState.allReviews.filter((review) => {
                return review.id !== action.payload.id
            });
            newState.allReviews = filteredReviews;

            const newById = { ...newState.byId };
            delete newById[action.payload.id];
            newState.byId = newById;

            return newState;
        }
        default: {
            return state;
        }
    }
}

export default reviewReducer;