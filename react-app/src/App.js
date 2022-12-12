import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Routes } from "react-router-dom";

import Header from "./components/Header/Header";
import Modals from "./components/Modals/Modals";
import ProductDetails from "./components/ProductDetails/ProductDetails";
import ProductGrid from "./components/ProductGrid/ProductGrid";
import { restoreUser } from "./store/session";
import OrderDetails from "./components/OrderDetails/OrderDetails";

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
        <Route path="/" element={<ProductGrid />} />
        <Route path="/products/:productId" element={<ProductDetails />} />
        <Route exact path='/purchases_reviews' element={<OrderDetails />} />
      </Routes>
    </>
  );
}
