import React from 'react';
import { useDispatch } from 'react-redux';
import { Modal } from '../../../context/Modal';
import { setEditReviewModal } from '../../../store/ui';
import EditReviewForm from './EditReviewForm';

export default function EditReviewFormModal() {
    const dispatch = useDispatch();

    return (
        <Modal onClose={() => dispatch(setEditReviewModal(false))}>
            <EditReviewForm />
        </Modal>
    );
}
