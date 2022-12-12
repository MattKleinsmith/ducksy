import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Routes } from "react-router-dom";

import Header from "./components/Header/Header";
import Modals from "./components/Modals/Modals";
import ProductDetails from "./components/ProductDetails/ProductDetails";
import ProductGrid from "./components/ProductGrid/ProductGrid";
import { restoreUser } from "./store/session";
import Orders from "./components/Orders/Orders";

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
        <Route path="/listing/:productId" element={<ProductDetails />} />
        <Route exact path='/your/purchases' element={<Orders />} />
        <Route exact path='/your/shop' element={<Orders />} />
      </Routes>
    </>
  );
}
