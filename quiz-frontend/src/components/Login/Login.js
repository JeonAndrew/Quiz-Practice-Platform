import React, { useState } from 'react';
import './Login.css';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Simulate sending login data to the server
    console.log('Logging in with:', { email, password });
    // Add API call here for real implementation
  };

  return (
    <div className='login-component'>
      <form onSubmit="nothing" className='login-form'>
        <h2>Login</h2>
        <label>Email:</label>
        <input 
          type="email" 
          value={email} 
          onChange={(e) => setEmail(e.target.value)} 
          required 
          className='login-form-input'
        />
        <label>Password:</label>
        <input 
          type="password" 
          value={password} 
          onChange={(e) => setPassword(e.target.value)} 
          required 
          className='login-form-input'
        />
        <button className='login-form-submit'>
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;
