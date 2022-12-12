import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Routes } from "react-router-dom";

import Header from "./components/Header/Header";
import Modals from "./components/Modals/Modals";
import ProductDetails from "./components/ProductDetails/ProductDetails";
import ProductGrid from "./components/ProductGrid/ProductGrid";
import { restoreUser } from "./store/session";
import OrderDetails from "./components/OrderDetails/OrderDetails";
import ShopManager from "./components/ShopManager/ShopManager";
import ProductEditor from "./components/ProductEditor/ProductEditor";
import { getProducts } from "./store/products";

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
        <Route path='/your/purchases' element={<OrderDetails />} />
        <Route path='/your/shop' element={<ShopManager />} />
        <Route path='/your/shop/listing/:productId' element={<ProductEditor />} />
      </Routes>
    </>
  );
}
