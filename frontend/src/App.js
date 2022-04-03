import React from 'react'
import logo from './logo.svg';
import './App.css';

import 'bootstrap/dist/css/bootstrap.min.css';

import {
  Card,
  Row,
  Col,
  Form,
  Container
} from 'react-bootstrap'

function App() {

  const [savings, setSavings] = React.useState()

  return (
    <Container>
      <Row>
        <Col md={6}>
          <Card>
            <Card.Header><h4>Calculator</h4></Card.Header>
            <Card.Body>
              <Form as={Row}>
                <Form.Group as={Col} md={12}>
                  <Form.Label>Savings</Form.Label>
                  <Form.Control type="number" value={savings} onChange={e => setSavings(e.target.value)} />
                  <Form.Text>How much do you have in savings?</Form.Text>
                </Form.Group>
                <Form.Group as={Col} md={6}>
                  <Form.Label>Going at it alone</Form.Label>
                  <Form.Control type="number" readOnly disabled value={savings ? savings * 10.0 : 0} />
                </Form.Group>
                <Form.Group as={Col} md={6}>
                  <Form.Label>Going at it with LongView</Form.Label>
                  <Form.Control type="number" readOnly disabled value={savings ? savings * 1.3 * 10.0 : 0} />
                </Form.Group>
              </Form>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default App;
