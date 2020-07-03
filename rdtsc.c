typedef unsigned long long __u64;
typedef unsigned long __u32;
int get_rdtsc(){
    __u32 hi,lo;
    __asm__ __volatile__ 
    (
        "rdtsc" : "=a" (lo),"=d"(hi)
    );
    return (__u64) hi<<32|lo;
}