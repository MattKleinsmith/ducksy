import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { getProducts } from "../../store/products";

import "./ProductEditor.css";

export default function ProductEditor() {
    const { productId } = useParams();
    const dispatch = useDispatch();
    const product = useSelector(state => state.products)[productId]

    useEffect(() => {
        dispatch(getProducts());
    }, [dispatch]);

    if (!product) return
    return (
        <div className="ProductEditorWrapper">
            <div className="ProductEditor">
                <h1>Editing product {productId}</h1>
            </div>
        </div>
    );
}
