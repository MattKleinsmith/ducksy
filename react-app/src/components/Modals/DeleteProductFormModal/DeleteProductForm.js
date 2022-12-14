import './DeleteProductForm.css';
import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from 'react-router-dom';
import { deleteProduct } from "../../../store/products";
import { setDeleteProductModal } from "../../../store/ui";

export default function DeleteProductForm() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const productId = useSelector(state => state.productDetails).id
    const [errors, setErrors] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();
        setErrors([]);
        return dispatch(deleteProduct(productId))
            .then(() => {
                dispatch(setDeleteProductModal(false));
                navigate("/");
            })
            .catch(errors => {
                console.log("3", errors);
                setErrors(Object.values(errors.errors))
            });
    };

    return (
        <form className="deleteForm" onSubmit={handleSubmit}>
            <h1 style={{ width: "300px" }}>Are you sure you want to delete this product?</h1>
            <ul>
                {errors.map((error, idx) => <li key={idx}>{error}</li>)}
            </ul>
            <button className="deleteFormButton" type="submit">Delete product</button>
        </form >
    );
}
