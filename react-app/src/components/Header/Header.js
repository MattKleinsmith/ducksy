// import { useSelector } from 'react-redux';
// import { useNavigate } from 'react-router-dom';

import './Header.css';
import Logo from './Logo';
import RightHeader from './RightHeader/RightHeader'

export default function Header() {
    // const ui = useSelector(state => state.ui);
    // const history = useNavigate();
    return (
        <>
            <div className="headerWrapper">
                <div className="header">
                    <Logo />
                    <RightHeader />
                </div>
            </div>
            <div className="line"></div>
        </>
    );
}
