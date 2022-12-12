import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { getProducts } from "../../store/products";

import "./ProductDetails.css";
import ProductDetailsLeft from "./ProductDetailsLeft/ProductDetailsLeft";
import ProductDetailsRight from "./ProductDetailsRight/ProductDetailsRight";

export default function ProductDetails() {
    const { productId } = useParams();
    const dispatch = useDispatch();
    const product = useSelector(state => state.products)[productId]

    useEffect(() => {
        dispatch(getProducts());
    }, [dispatch]);

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
