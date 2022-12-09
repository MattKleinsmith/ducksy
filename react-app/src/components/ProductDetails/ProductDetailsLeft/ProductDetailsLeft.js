import "./ProductDetailsLeft.css"
import ProductDetailsImages from "./ProductDetailsImages/ProductDetailsImages";
import ProductDetailsReviewList from "./ProductDetailsReviewList/ProductDetailsReviewList";

export default function ProductDetailsLeft({ product }) {
    return (
        <div className="ProductDetailsLeftWrapper">
            <div className="ProductDetailsLeft">
                <ProductDetailsImages product={product} />
                <ProductDetailsReviewList product={product} />
            </div>
        </div>
    );
}
