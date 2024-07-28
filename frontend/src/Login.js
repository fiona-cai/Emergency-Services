import React from 'react';
import firefighters from './firefighters.png';
import title from './title.png';
import subtitle from './subtitle.png';

function Login() {
    return (
        <>
            <img src={firefighters} alt="firefighters" className="firefighters"/>
            <div className="loginContainer">
                <div className="loginTitleContainer">
                    <span className="loginTitle">Welcome to </span><span className="loginTitle" style={{"color": "#4EAE50"}}>CrisisControl</span>
                </div>
                <p className="loginSubtitle">Making emergency contacts a smoother process</p>
                <p className="loginSubtitle" style={{"marginTop": "70px", "color": "black"}}>ID: </p>
                <form className="input"></form>
                <p className="loginSubtitle" style={{"marginTop": "35px", "color": "black"}}>Password: </p>
                <form className="input"></form>
            </div>
        </>
    );
}

export default Login;