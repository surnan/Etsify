//Constants
const GET_USER = 'user/GET_USER';

//Action Creators
const getUser = (user) => ({
    type: GET_USER,
    payload: user
});

//Thunks
// export const getUserThunk = (userId) => async (dispatch) => {
//     const response = await fetch(`/api/users/${userId}`);

//     if (response.ok) {
//         const user = await response.json();
//         dispatch(getUser(user));
//     }
// };

export const getUserThunk = (userId) => async (dispatch) => {
    try {
        const response = await fetch(`/api/users/${userId}`);

        if (response.ok) {
            const user = await response.json();
            dispatch(getUser(user));
        } else {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to fetch user');
        }
    } catch (error) {
        console.error('Error in getUserThunk:', error);
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