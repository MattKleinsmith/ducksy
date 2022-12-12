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
import ShoppingCart from "./components/ShoppingCart/ShoppingCart";

export default function App() {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(restoreUser());
  }, [dispatch]);

  return (
    <>
      <Modals />
      <Header />
      <Routes>
        <Route exact path="/" element={<ProductGrid />} />
        <Route path="/listing/:productId" element={<ProductDetails />} />
        <Route exact path='/your/purchases' element={<OrderDetails />} />
        <Route exact path='/your/shop' element={<ShopManager />} />
        <Route path='/cart' element={<ShoppingCart />} />
      </Routes>
    </>
  );
}
