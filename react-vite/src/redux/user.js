//Constants
const GET_USER = 'user/GET_USER';

//Action Creators
const getUser = (user) => ({
    type: GET_USER,
    payload: user
});

//Thunks
export const getUserThunk = (userId) => async (dispatch) => {
    const response = await fetch(`/api/users/${userId}`);

    if (response.ok) {
        const user = await response.json();
        dispatch(getUser(user));
    }
};

//Reducer
const initialState = {};

function userReducer(state = initialState, action) {
    switch (action.type) {
        case GET_USER:
            return { ...state, reviewUser: action.payload };
        default:
            return state;
    }
}

export default userReducer;