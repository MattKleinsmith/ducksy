import { Route, Routes } from "react-router-dom";
import ProductDetails from "./components/ProductDetails/ProductDetails";
import ProductGrid from "./components/ProductGrid/ProductGrid";
import Purchases from "./components/Purchases/Purchases";
import ShopManager from "./components/ShopManager/ShopManager";
import ProductEditor from "./components/ProductEditor/ProductEditor";
import ShoppingCart from "./components/ShoppingCart/ShoppingCart";
import Homepage from "./components/Homepage/Homepage";
import OrderConfirmation from "./components/ShoppingCart/CartCheckout/OrderConfirmation/OrderConfirmation";

export default function AppRoutes() {
    return (
        <Routes>
            <Route path="/" element={<Homepage />} />

            <Route path="/listings" element={<ProductGrid />} />

            <Route path="/listing/:productId" element={<ProductDetails />} />
            <Route path="/category/:categoryName" element={<ProductGrid />} />
            <Route path="/your/purchases" element={<Purchases />} />

            <Route path="/your/shop" element={<ShopManager />} />
            <Route path="/your/shop/listing/new" element={<ProductEditor />} />
            <Route path="/your/shop/listing/:productId" element={<ProductEditor />} />

            <Route path="/cart" element={<ShoppingCart />} />
            <Route path="/cart/checkout/:orderId" element={<OrderConfirmation />} />
        </Routes>
    );
}
