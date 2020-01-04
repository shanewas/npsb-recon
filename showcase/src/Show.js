import React, { Component } from "react";
import Data from "./ATM_JSON/AccuringNotOnBB.json";

export default class Show extends Component {
	getData() {
		console.log(Data);
	}
	componentDidMount() {
		this.getData();
	}
	render() {
		return (
			<React.Fragment>
				<div className='container-fluid'>
					<table className='table'>
						<thead className="thead-dark">
							<tr>
                                {/* DOnt delete Important */}
                                {/* {Object.keys(Data[0]).map(e => {return <th scope="col">{e}</th>})} */}
                                <th>No.</th>
								<th scope='col'>Date & Time</th>
								<th scope='col'>PAN</th>
								{/* <th scope='col'>FROMACCT</th> */}
								<th scope='col'>TRANCODE</th>
								{/* <th scope='col'>TYPE</th> */}
								<th scope='col'>TERMNAME</th>
								<th scope='col'>TERMPSNAME</th>
								<th scope='col'>AUTHFINAME</th>
								<th scope='col'>TRANNUMBER</th>
								<th scope='col'>EXTRRN</th>
								<th scope='col'>APPROVALCODE</th>
								<th scope='col'>TERMSIC</th>
								<th scope='col'>TERMOWNER</th>
								{/* <th scope='col'>TERMRETAILERNAME</th> */}
								<th scope='col'>CURRENCY</th>
								<th scope='col'>AMOUNT</th>
								{/* <th scope='col'>RESPCODE</th> */}
								<th scope='col'>SRVC</th>
								<th scope='col'>CPID</th>
							</tr>
						</thead>
						<tbody>
							{Data.map((data, index) => {
								return (
									<tr>
                                        <td>{index}</td>
										<td>{data.DATE_TIME_x}</td>
										<td>{data.PAN}</td>
										{/* <td>{data.FROMACCT}</td> */}
										<td>{data.TRANCODE}</td>
										{/* <td>{data.TYPE}</td> */}
										<td>{data.TERMNAME_x}</td>
										<td>{data.TERMPSNAME}</td>
										<td>{data.AUTHFINAME}</td>
										<td>{data.TRANNUMBER_x}</td>
										<td>{data.EXTRRN}</td>
										<td>{data.APPROVALCODE}</td>
										<td>{data.TERMSIC_x}</td>
										<td>{data.TERMOWNER}</td>
										{/* <td>{data.TERMRETAILERNAME_x}</td> */}
										<td>{data.CURRENCY_x}</td>
										<td>{data.AMOUNT}</td>
										{/* <td>{data.RESPCODE}</td> */}
										<td>{data.SRVC}</td>
										<td>{data.CPID}</td>
									</tr>
								);
							})}
						</tbody>
					</table>
				</div>
			</React.Fragment>
		);
	}
}
