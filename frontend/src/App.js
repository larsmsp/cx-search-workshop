import React, { Component } from 'react';
import { Container, Header } from 'semantic-ui-react'
import SearchUI from './components/SearchUI.js'
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <Container textAlign={'center'}>
        <Header as='h2'>Search Computas.com</Header>
        <SearchUI />
      </Container>
    );
  }
}

export default App;
