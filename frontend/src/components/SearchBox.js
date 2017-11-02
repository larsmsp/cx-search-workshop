import React, { Component } from 'react'
import { Input, Grid, Button, Loader } from 'semantic-ui-react'
import SearchResults from './SearchResult'

export default class SearchBox extends Component {
    
    componentWillMount() {
        this.resetComponent()
    }

    resetComponent = () => this.setState({ isActive: false,
        results: [],
        query: '',
        endpoint: '',
        title: '',
        contents: '',
        url: ''})

    handleSearchResponse = (json) => {
        this.setState({
            isActive: false,
            results: json,
        })
    }

    handleSearchError = (err) => {
        this.setState({
            isActive: false,
            results: []
        })
    }

    handleSearchChange = (e, value) => {
        this.setState({ isActive: true, value })

        setTimeout(() => {
            if (this.state.query.length < 1) {
                return this.resetComponent()
            }

            if (this.state.query.length >= 3) {
                let query = encodeURI(this.state.query.replace(/\s/gi, '+'))
                fetch(`/search?q=${ query }`, {
                    method: 'GET'
                }).then(function(response) {
                    if (response.ok) {
                        return response.json()
                    }
                    throw Error(response.status.toString())
                }).then((json) => this.handleSearchResponse(json))
                .catch((err) => this.handleSearchError(err))
            }
        }, 1)
    }

    handleQueryChange = (e, data) => {
        this.setState({ query: data.value })
    }

    handleTitleChange = (e, data) => {
        this.setState({ title: data.value })
    }

    handleContentsChange = (e, data) => {
        this.setState({ contents: data.value })
    }

    handleURLChange = (e, data) => {
        this.setState({ url: data.value })
    }

    render() {
        const { results, isActive } = this.state

        return (
            <Grid textAlign={'center'}>
                <Grid.Row>
                    <Input label={'Query'} onChange={this.handleQueryChange} size={'large'} />
                    <Button primary content={'Search'} size={'large'} onClick={this.handleSearchChange} />
                </Grid.Row>
                <Grid.Row>
                    <Input label={'Title'} onChange={this.handleTitleChange} size={'large'} />
                </Grid.Row>
                <Grid.Row>
                    <Input label={'Contents'} onChange={this.handleContentsChange} size={'large'} />
                </Grid.Row>
                <Grid.Row>
                    <Input label={'URL'} onChange={this.handleURLChange} size={'large'} />
                </Grid.Row>
                <Grid.Row>
                    <Button primary content={'Insert'} size={'large'} onClick={this.handleSearchChange} />
                </Grid.Row>
                <Grid.Row>
                    <Loader content={'Searching...'} active={isActive} size={'huge'} />
                    <SearchResults results={results} />
                </Grid.Row>
            </Grid>
        )
    }
}