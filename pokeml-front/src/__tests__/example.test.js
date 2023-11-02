// This is a sample unit test to check if sonar works properly
import { sum } from '../example.js'
import { expect, test } from 'vitest'

test('check add function', () => {
    expect(sum(1, 2)).toBe(3)
})