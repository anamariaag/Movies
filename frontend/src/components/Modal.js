import React, { Fragment } from "react";
import styled from "styled-components";

const Modal = ({ children, estado, cambiarEstado }) => {
    return (
        <>
            {estado &&
                <Overlay>
                    <ContenedorModal>
                        <BotonCerrar onClick={() => cambiarEstado(false)}>X</BotonCerrar>
                        {children}
                    </ContenedorModal>
                </Overlay>
            }
        </>
    );
}

export default Modal;

const Overlay = styled.div`
    width: 100vw;
    height: 100vh; 
    position: fixed;
    top: 0;
    left: 0;
    background-color: rgba(0, 0, 0, 0.5); 

    display: flex;
    align-items: center;
    justify-content: center;
`;

const ContenedorModal = styled.div`
    width: 60%;
    height: 70%; 
    position: relative;
    border-radius: 5px;
    box-shadow: rgba(100,100,111,0.2) 0px 7px 29px 0px;
    background: #4F4F4F; 
    padding: 20px
`;

const BotonCerrar = styled.button` 
    position: absolute;
    top: 20px;
    right: 20px;
    width: 30px; /* Corregido de "wigth" a "width" */
    height: 30px;
    border: none;
    background: none; 
    cursor: pointer;
    transition: .3s ease all;
    border-radius: 5px;
    color: #1766DC;

    &:hover {
        background: #f2f2f2;
    }
`;

