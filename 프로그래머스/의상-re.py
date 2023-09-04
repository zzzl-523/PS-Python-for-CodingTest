function solution(clothes) {
    let category = {};
    let result = 1;
    clothes.forEach((v) => category[v[1]] = (category[v[1]] || 0) + 1);
    for(let v in category) result *= (category[v] + 1);
    return result - 1;
}