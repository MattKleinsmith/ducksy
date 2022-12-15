// import { useSelector } from 'react-redux';
// import { useNavigate } from 'react-router-dom';

import './Header.css';
import Logo from './Logo';
import RightHeader from './RightHeader/RightHeader'
import SearchBar from './SearchBar/SearchBar';

export default function Header() {
    // const ui = useSelector(state => state.ui);
    // const history = useNavigate();
    return (
        <>
            <div className="headerWrapper">
                <div className="header">
                    <Logo />
                    <SearchBar />
                    <RightHeader />
                </div>
            </div>
            <div className="line"></div>
        </>
    );
}
