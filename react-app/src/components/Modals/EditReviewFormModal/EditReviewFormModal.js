import React from 'react';
import { useDispatch } from 'react-redux';
import { Modal } from '../../../context/Modal';
import { setReviewModal } from '../../../store/ui';
import EditReviewForm from './EditReviewForm';

export default function ReviewFormModal() {
    const dispatch = useDispatch();

    return (
        <Modal onClose={() => dispatch(setReviewModal(false))}>
            <EditReviewForm />
        </Modal>
    );
}
