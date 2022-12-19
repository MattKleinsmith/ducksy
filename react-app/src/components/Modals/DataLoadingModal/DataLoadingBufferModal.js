import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router';
import { Modal } from '../../../context/Modal';
import { setDataLoadingModal } from '../../../store/ui';
import DataLoadingBuffer from './DataLoadingBuffer';

export default function DataLoadingBufferModal() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    return <Modal onClose={() => {
        dispatch(setDataLoadingModal(false))
        navigate('/')
    }}>
        <DataLoadingBuffer />
    </Modal>;
}
