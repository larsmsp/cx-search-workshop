import React, { Component } from 'react'
import ReactMarkdown from 'react-markdown'
import { Item } from 'semantic-ui-react'

import 'semantic-ui/dist/semantic.css'


const SearchResult = ({ title, url, highlight }) => (
    <Item>
        <Item.Content>
            <Item.Header as='a' href={url}>{title}</Item.Header>
            <Item.Meta>{url}</Item.Meta>
            <Item.Description dangerouslySetInnerHTML={{ __html: highlight }}></Item.Description>
        </Item.Content>
        <hr />
    </Item>
)

export default class SearchResults extends Component {

    render() {
        let items = []
        this.props.results.forEach(function(element) {
            items.push(<SearchResult key={element.url} title={element.title} url={element.url} highlight={element.contents} />)
        }, this);
        return (
            <Item.Group>
                {items}
            </Item.Group>
        )
    }
}