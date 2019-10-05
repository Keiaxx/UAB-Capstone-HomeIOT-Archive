import React, { Component } from "react";
import ToggleButtonGroup from "react-bootstrap/ToggleButtonGroup";
import ToggleButton from "react-bootstrap/ToggleButton";
import ButtonGroup from "@material-ui/core/ButtonGroup";
/*
I use react bootstrap fot the buttons.
npm react-bootstrap
Public link:
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous" />

Radio Button types. 
*/
export default class Table extends Component {

    render() {
        return (
            <div >
                <div id="Tittle">
                    <p>
                        <h1>The Switchanater!</h1>
                    </p>
                </div>
                <tbody id="body">
                    <tr >
                        <th scope="row">Kitchen</th>
                        <td>
                            <ButtonGroup>
                                <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                    <ToggleButton value={1}>ON</ToggleButton>
                                    <ToggleButton id="BedroomLights" value={1}>
                                        Dishwasher
                </ToggleButton>
                                    <ToggleButton value={3}>OFF</ToggleButton>
                                </ToggleButtonGroup>
                            </ButtonGroup>
                        </td>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Lights
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Oven
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Microwave
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Washing Machine
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Dryer
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Refrigerator
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Stove
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Bathrooom One</th>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Exhast Fan
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Lights
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Bathrooom Two</th>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Exhast Fan
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Lights
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                    </tr>

                    <tr>
                        <th scope="row">Living Room</th>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Lights
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Lamps
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    TV
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Master Bedroom</th>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Lights
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Lamps
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    TV
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Bedroom</th>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Lights
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Lamps
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Guest Bedroom</th>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Lights
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                        <td>
                            <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
                                <ToggleButton value={1}>ON</ToggleButton>
                                <ToggleButton id="BedroomLights" value={1}>
                                    Lamps
                </ToggleButton>
                                <ToggleButton value={3}>OFF</ToggleButton>
                            </ToggleButtonGroup>
                        </td>
                    </tr>
                </tbody>
            </div>
        );
    }
}

