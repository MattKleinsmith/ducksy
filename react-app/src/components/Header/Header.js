import styles from './Header.module.css';
import Logo from './Logo';
import RightHeader from './RightHeader/RightHeader'
import SearchBar from './SearchBar/SearchBar';

export default function Header() {
    return (
        <>
            <div className={styles.headerWrapper}>
                <div className={styles.header}>
                    <Logo />
                    <SearchBar />
                    <RightHeader />
                </div>
            </div>
            <div className={styles.line}></div>
        </>
    );
}
