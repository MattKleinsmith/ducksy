import "./RightHeader.css";
import { useDispatch, useSelector } from "react-redux";
import ProfileButton from "./ProfileButton/ProfileButton";
import CartButton from "./CartButton/CartButton";
import { setSigninModal } from "../../../store/ui";

export default function RightHeader() {
    const session = useSelector(state => state.session);
    const dispatch = useDispatch();
    return <span>
        {<div className="rightHeader">
            {!session.user && <div className="pointer" onClick={() => dispatch(setSigninModal(true))}>Sign In</div>}
            {session.user && <ProfileButton />}
            <CartButton />
        </div>}
    </span>
}
