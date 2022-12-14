import "./DropdownProfile.css";
import DropdownSignedIn from "./DropdownSignedIn";

export default function DropdownProfile({ user, ui }) {
    return <>
        <div className={"profile-dropdown"}>
            <DropdownSignedIn user={user} />
        </div>
    </>
}
