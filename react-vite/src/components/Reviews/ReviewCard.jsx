const ReviewCard = ({rev}) => {
    return (
        <>
        <h3>{rev.stars}</h3>
        <p>{rev.review}</p>
        </>
        
    )
};

export default ReviewCard