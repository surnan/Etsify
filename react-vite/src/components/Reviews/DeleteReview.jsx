// import {useState} from 'react';
import {useDispatch} from 'react-redux'
import { useParams } from 'react-router-dom';
import {deleteReviewThunk} from '../../redux/review';
const DeleteReview = () =>{
    let {reviewId} = useParams();
    // let review = useSelector((state) => state.reviews.byId[reviewId]);
    const dispatch = useDispatch();
    dispatch(deleteReviewThunk(reviewId));
    return<>
    <h2>Review Deleted</h2>
    </>
}

export default DeleteReview;