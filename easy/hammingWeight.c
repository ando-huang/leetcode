int hammingWeight(uint32_t n){
    int count = n ? 1:0;
    while(n&=(n-1))
        count += 1;
    return count;
}
