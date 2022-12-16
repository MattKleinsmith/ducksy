import styles from "./DropdownProfile.module.css";
import DropdownSignedIn from "./DropdownSignedIn";

export default function DropdownProfile({ user, ui }) {
    return <>
        <div className={styles.profileDropdown}>
            <DropdownSignedIn user={user} />
        </div>
    </>;
}
