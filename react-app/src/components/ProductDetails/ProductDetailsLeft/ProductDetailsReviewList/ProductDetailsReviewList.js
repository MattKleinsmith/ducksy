import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getReviewsByProductId } from "../../../../store/reviews";
import ProductDetailsReview from "./ProductDetailsReview/ProductDetailsReview";
import "./ProductDetailsReviewList.css"

export default function ProductDetailsReviewList({ product }) {
    const dispatch = useDispatch();
    const reviews = useSelector(state => Object.values(state.reviews));
    useEffect(() => {
        dispatch(getReviewsByProductId(product.id));
    }, [dispatch, product.id]);

    if (!reviews) return;
    return (
        <div className="ProductDetailsReviewListWrapper">
            <div className="ProductDetailsReviewList">
                {reviews.map((review, i) => <ProductDetailsReview key={i} review={review} />)}
            </div>
        </div>
    );
}
