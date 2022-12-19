import { Modal } from '../../../context/Modal';
import DataLoadingBuffer from './DataLoadingBuffer';

export default function DataLoadingBufferModal() {
    return <Modal onClose={() => { }}>
        <DataLoadingBuffer />
    </Modal>;
}
