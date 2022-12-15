import { useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import "./ProductDetails.css";
import ProductDetailsLeft from "./ProductDetailsLeft/ProductDetailsLeft";
import ProductDetailsRight from "./ProductDetailsRight/ProductDetailsRight";

export default function ProductDetails() {
    const { productId } = useParams();
    const product = useSelector(state => state.products)[productId]

    if (!product) return
    return (
        <div className="ProductDetailsWrapper">
            <div className="ProductDetails">
                <ProductDetailsLeft product={product} />
                <ProductDetailsRight product={product} />
            </div>
        </div>
    );
}
