import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Routes } from "react-router-dom";

import Header from "./components/Header/Header";
import Modals from "./components/Modals/Modals";
import ProductDetails from "./components/ProductDetails/ProductDetails";
import ProductGrid from "./components/ProductGrid/ProductGrid";
import { restoreUser } from "./store/session";
import Purchases from "./components/Purchases/Purchases";
import ShopManager from "./components/ShopManager/ShopManager";
import ProductEditor from "./components/ProductEditor/ProductEditor";
import { getProducts } from "./store/products";
import ShoppingCart from "./components/ShoppingCart/ShoppingCart";

export default function App() {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(restoreUser());
    dispatch(getProducts());
  }, [dispatch]);


  return (
    <>
      <Modals />
      <Header />
      <Routes>
        <Route path="/" element={<ProductGrid />} />
        <Route path="/listing/:productId" element={<ProductDetails />} />
        <Route path='/your/purchases' element={<Purchases />} />
        <Route path='/your/shop' element={<ShopManager />} />
        <Route path='/your/shop/listing/new' element={<ProductEditor />} />
        <Route path='/your/shop/listing/:productId' element={<ProductEditor />} />
        <Route path='/cart' element={<ShoppingCart />} />
      </Routes>
    </>
  );
}
