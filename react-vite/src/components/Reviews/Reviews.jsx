import { useEffect} from 'react';
import { useDispatch, useSelector } from 'react-redux';
import ReviewCard from './ReviewCard';
import { getReviewsAllThunk } from '../../redux/store/review';


const Reviews = ({product}) => {
  const dispatch = useDispatch();

//   let sessionUser = useSelector((state) => state.session.user);

  let reviews = useSelector((state) => state.reviews.allReviews);
  useEffect(() => {
    dispatch(getReviewsAllThunk({product}));
  }, [dispatch, product])



  const productReviews = productReviews ? productReviews.find(review => {return review.productId === product.id}) : undefined;

  return (
    <>
      <div className = "reviews">
        {productReviews.map((review) => <ReviewCard rev = {review} key = {review.id}/>)}
        {productReviews.length < 1 ? <p>Be the first to post a review!</p> : ""}
      </div>

   
    </>
  )
}

export default Reviews;
